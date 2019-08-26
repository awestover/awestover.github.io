function realMod(n, m) {
  return ((n % m) + m) % m;
}

class Mover {
	constructor(name, speed) {
		this.speed = speed;
		this.th = 2*Math.PI*Math.random();
		this.img = $("#" + name);
		this.img.css("position", "absolute");
		this.animateCt = 0;
		this.resetAnimateCt = 400;
		this.sightRadius = 300;
		this.seekOrFlee = false;
	}
	move() {  // only ever specify top and left to avoid ambiguity
		let currentLoc = this.img.position();
		let dPos = [Math.cos(this.th)*this.speed, Math.sin(this.th)*this.speed];
		let newLoc = [dPos[0]+currentLoc.left, dPos[1]+currentLoc.top];
		newLoc[0] = realMod(newLoc[0], $("body").width());
		newLoc[1] = realMod(newLoc[1], $("body").height());
		this.img.css({"left":newLoc[0], "top":newLoc[1]})
		if(dPos[0] < 0){
			this.img.css("transform", "scale(-1,1)");
		}
		else{
			this.img.css("transform", "scale(1,1)");
		}
		if (!this.seekOrFlee){
			this.animateCt+=1;
			if (this.animateCt > this.resetAnimateCt){
				this.th = Math.random()*Math.PI*2;
				this.animateCt = this.resetAnimateCt*0.7*Math.random();
			}
		}
	}
	seek(other) {
		let dx = other.img.position().left - this.img.position().left;
		let dy = other.img.position().top - this.img.position().top;
		if (true || dx*dx + dy*dy < this.sightRadius*this.sightRadius) {
			this.th = Math.atan2(dy, dx);
			this.seekOrFlee = true;
		}
		else {
			this.seekOrFlee = false;
		}
	}
	die(other){
		let dx = other.img.position().left - this.img.position().left;
		let dy = other.img.position().top - this.img.position().top;
		if(dx*dx+dy*dy < this.img.width()*this.img.width()){
			this.img.css({"left":$("body").width()*Math.random(), "top":$("body").height()*Math.random()});
		}

	}
	animate(){
		this.move();
		setTimeout(() => {this.animate()}, 20);
	}

}

let dog = new Mover("dog", 2.0);
let dino = new Mover("dino", 2.5);
dog.animate();
dino.animate();
setInterval(function(){dino.seek(dog);}, 100); 
setInterval(function(){dog.die(dino);}, 100); 


