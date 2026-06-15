var fs=require('fs');
var c=fs.readFileSync('d:/Documents/CodeBuddy Files/北京游/index.html','utf8');
var m=c.match(/<script>\r?\n([\s\S]*?)\r?\n<\/script>/);
var js=m[1];
var lines=js.split('\r\n');
for(var i=1268;i<Math.min(1276,lines.length);i++){
  console.log((i+1)+': '+(lines[i]||'').substring(0,80));
}
