//atvdd1
// let numerosDaSorte = [37, 14, 26, 5, 94, 87];

 
// for(let i = 0; i <= numerosDaSorte.length; i++){
//  let num = numerosDaSorte[i];

//    if (num %2 === 0 && num < 50){
//       console.log(num + " O número é par e menor que 50");
//     }else if (num < 50){
//       console.log(num + " O número é menor que 50");
//     }else{
//       console.log(num + " O número é maior que 50");
//     }
// }

//atvdd2
//console.log("Conexão foi feita com SUCESSO!!")

//atvdd3
let h1txt = document.getElementById("titulo");
let atxt = document.querySelectorAll(".link") 
let oladd=document.querySelector("#lista-ordenada")

h1txt.innerText = "ProzEdu";
atxt[0].innerText="ProzEdu";
atxt[1].innerText="Facebook"

oladd.innerHTML =`
<li> Hello world!!!, I'm tired of saying this</li>
<li>Sed ut perspiciatis unde omnis iste natus error sit voluptatem</li>
<li>doloremque laudantium, totam rem aperiam, eaque ipsa</li>
<li>et quasi architecto beatae vitae dicta sunt explicabo</li>
<li>sed quia non numquam eius modi tempora incidunt ut labore et</li>
<li>Quis autem vel eum iure reprehenderit qui in ea voluptate </li>
`
