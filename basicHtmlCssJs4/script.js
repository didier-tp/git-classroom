window.onload= ()=>{
	
	document.getElementById("btnAdd")
	     .addEventListener("click" , ()=>{
	   let a = Number(document.getElementById("a").value);
	   let b = Number(document.getElementById("b").value);
	   let res=a+b;
	   document.getElementById("spanRes").innerHTML=res;
	});
	
}
