let num1 = 0;
let num2 = 0;
let oper = 0;


function conta(num1,num2, oper){
  if (oper === 1){
    return  num1 + num2;
  } else if(oper === 2){
    return num1 - num2;
  }else if (oper===3){
    return num1 * num2;
  }else if(oper===4){
    return num1 / num2;
  }
}
let resp = conta(24,2,3);
let templateresp = `O resultado da operação foi: ${resp}`
console.log(templateresp)