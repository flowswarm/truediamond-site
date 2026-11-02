/* True Diamond Life Care Group — site behaviour */
(function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('open') ? 'true' : 'false');
    });
  }

  // Dropdowns on mobile: tap parent to expand
  document.querySelectorAll('.nav .has-sub > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.matchMedia('(max-width: 1060px)').matches) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.parentElement;
      var isOpen = item.classList.contains('open');
      item.classList.toggle('open', !isOpen);
      btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  });

  // Forms: submit to Web3Forms in the background, show the result inline.
  // Emails go to the address the access key was issued for (owner@truediamondlcg.com).
  document.querySelectorAll('form.js-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.querySelector('.form-success');
      var err = form.querySelector('.form-error');
      var btn = form.querySelector('button[type="submit"]');
      if (ok) ok.classList.remove('show');
      if (err) err.classList.remove('show');
      if (!form.checkValidity()) { form.reportValidity(); return; }

      // Tell Web3Forms where to send the visitor back to after a regular (non-background) post.
      var nextInput = form.querySelector('input[name="redirect"]');
      if (!nextInput) {
        nextInput = document.createElement('input');
        nextInput.type = 'hidden'; nextInput.name = 'redirect';
        form.appendChild(nextInput);
      }
      nextInput.value = location.origin + location.pathname + '?sent=1#' + (form.closest('section') && form.closest('section').id ? form.closest('section').id : 'contact');

      var data = new FormData(form);
      data.append('page', document.title);
      var ajaxUrl = form.getAttribute('action');
      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      var fallback = function () {
        // Background send failed or timed out — do a regular form post instead so the
        // message still goes through; Web3Forms redirects back here with ?sent=1.
        if (location.protocol === 'file:') {
          if (err) err.classList.add('show');
          if (btn) { btn.disabled = false; btn.textContent = label; }
        } else {
          HTMLFormElement.prototype.submit.call(form);
        }
      };

      var controller = ('AbortController' in window) ? new AbortController() : null;
      var timer = setTimeout(function () { if (controller) controller.abort(); else fallback(); }, 8000);

      fetch(ajaxUrl, { method: 'POST', body: data, headers: { 'Accept': 'application/json' }, signal: controller ? controller.signal : undefined })
        .then(function (r) { return r.json().then(function (j) { return { okStatus: r.ok, body: j }; }); })
        .then(function (res) {
          clearTimeout(timer);
          if (res.okStatus && String(res.body.success) === 'true') {
            if (ok) ok.classList.add('show');
            form.reset();
            if (btn) { btn.disabled = false; btn.textContent = label; }
          } else {
            throw new Error(res.body.message || 'send failed');
          }
        })
        .catch(function () { clearTimeout(timer); fallback(); });
    });
  });

  // Returned from a regular Web3Forms post (?sent=1): show the thank-you message.
  if (/[?&]sent=1/.test(location.search)) {
    var target = null;
    if (location.hash) { var sec = document.querySelector(location.hash); if (sec) target = sec.querySelector('form.js-form'); }
    if (!target) target = document.querySelector('form.js-form');
    if (target) {
      var okMsg = target.querySelector('.form-success');
      if (okMsg) okMsg.classList.add('show');
      target.scrollIntoView({ block: 'center' });
    }
    try { history.replaceState(null, '', location.pathname + location.hash); } catch (e) {}
  }

  // Mark the current page in the nav
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a, .side-nav a').forEach(function (a) {
    var href = a.getAttribute('href') || '';
    if (href.split('#')[0] === here && href.indexOf('#') === -1) {
      a.parentElement.classList.add('active');
    }
  });

  // Footer year
  var y = document.querySelector('[data-year]');
  if (y) { y.textContent = new Date().getFullYear(); }
})();
