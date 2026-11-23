const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const f of process.argv.slice(2)) {
    const pg = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
    await pg.goto('file://' + path.resolve(f)); await pg.evaluate(() => document.fonts.ready);
    await pg.waitForTimeout(300);
    await pg.screenshot({ path: f.replace('.html', '.png') }); await pg.close();
  }
  await b.close();
})();
