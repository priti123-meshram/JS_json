// const text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
// const obj = JSON.parse(text);

// console.log( obj)


// const fs=require('fs');
// const text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
// const obj = JSON.parse(text);
// // console.log( obj)
// const file=fs.writeFileSync("parse2.json",(text))

// const jsonData = '{ "name":"priti", "age": 22 }'
// const obj = JSON.parse(jsonData);
// console.log(obj); 

// const fs=require('fs');
// const jsonData = '{ "name":"priti", "age": 22 }'
// const obj = JSON.parse(jsonData);
// // console.log(obj); // John

// const file=fs.writeFileSync("parse1.json",(jsonData))


var fs=require('fs');
var n='{"a":1,"b":5,"c":9}'
var c=JSON.parse(n)
var files=fs.writeFileSync("priti.json",(n))





var fs=require('fs');
var a={one:"preeti",two:"sonam",three:"sangeeta"}
var n=JSON.stringify(a);
var file=fs.writeFileSync("priti2.json",JSON.stringify(a))
