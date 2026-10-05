/* Privacy notice. The site sets no cookies and runs no analytics; the in-page
   demo keeps its sample books in the visitor's own browser. This tells them so
   once, and remembers the dismissal the same way (localStorage, nothing sent). */
(function () {
  var KEY = 'ct_notice_seen';
  try { if (localStorage.getItem(KEY)) return; } catch (e) {}
  var el = document.createElement('aside');
  el.className = 'notice'; el.setAttribute('role', 'region'); el.setAttribute('aria-label', 'Privacy notice');
  el.innerHTML = '<b>No cookies. No tracking.</b>' +
    '<p>This site sets no cookies and runs no analytics. The in-page demo keeps its sample books in your browser only, and nothing leaves your device.</p>' +
    '<div class="row"><a href="https://privacy.crehztracker.com">Privacy policy</a><button type="button" class="btn btn-copper">Got it</button></div>';
  document.body.appendChild(el);
  requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('on'); }); });
  el.querySelector('button').addEventListener('click', function () {
    try { localStorage.setItem(KEY, '1'); } catch (e) {}
    el.classList.remove('on'); setTimeout(function () { el.remove(); }, 400);
  });
})();
