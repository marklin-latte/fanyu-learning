/* 
task3: 使用 orders 的資料整理成 sql 用的語法。
預設執行指令 node W1/task2.js 輸出結果為:
INSERT INTO Order (price, count) VALUES (1000, 2),(2000,2),(2000,3)

參考資料: 
https://www.w3schools.com/js/js_loop_for.asp
https://www.w3schools.com/js/js_string_templates.asp
*/ 

var orders = [
  {
    price: 1000,
    count: 2
  },{
    price: 2000,
    count: 2
  },{
    price: 2000,
    count: 3
  }
];

// ==================================
var sql = '';



// ==================================
// 將結果輸出
console.log(sql);