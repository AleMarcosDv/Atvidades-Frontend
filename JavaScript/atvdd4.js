let num1 = 0;
let num2 = 0;
let oper = 0;
let op = String;
let error = false

function conta(num1,num2, oper){
  if (oper === 1){
    op = "+";
    return  num1 + num2;
  } else if(oper === 2){
    op = "-";
    return num1 - num2;
  }else if (oper===3){
    op = "*";
    return num1 * num2;
  }else if(oper===4){
    op = "/";
    return num1 / num2;
  }else{
    console.log("opção indisponivel")
    return error = true;
  }
}
let n1 = 24;
let n2 = 2;
let np = 5;
let resp = conta(n1,n2,np);
if (error) {
  console.log("ERROR")
}else{
  let templateresp = `O resultado da operação: ${n1} ${op} ${n2} foi: ${resp}`
  console.log(templateresp)
}