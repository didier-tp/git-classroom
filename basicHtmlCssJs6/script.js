window.onload= ()=>{
	
	document.getElementById("btnAdd")
	     .addEventListener("click" , ()=>{
	   let a = Number(document.getElementById("a").value);
	   let b = Number(document.getElementById("b").value);
	   let c = Number(document.getElementById("c").value);
	   let res=a+b+c;
	   document.getElementById("spanRes").innerHTML=res;
	});
	
}
