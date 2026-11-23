const {chromium}=require('playwright');const path=require('path');
(async()=>{const [,,h,o,w,ht]=process.argv;const b=await chromium.launch();
const p=await b.newPage({viewport:{width:+w,height:+ht},deviceScaleFactor:2});
await p.goto('file://'+path.resolve(h));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:o,clip:{x:0,y:0,width:+w,height:+ht}});await b.close();})();
