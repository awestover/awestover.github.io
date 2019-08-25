$("#dog").css("position", "absolute");

function moveUp(){
	let currentLoc = $("#dog").position().top;
	if(currentLoc < 0){
		currentLoc = 1000;
	}
	$("#dog").css("top", (currentLoc-10)+"px");
}

function animateDog(){
	moveUp();
	setTimeout(animateDog,50);
}

animateDog();

