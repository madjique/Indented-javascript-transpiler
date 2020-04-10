//this is a classic function
function A(){
    console.log("function A")
}
//this is an arrow function
const arrowfunc = (e) => {
    if (e > 0) {
        console.log("greater than 0")
	}
    else {
        console.log("negative")
	}
}
//this is an object JSON
obj = {
    id : 0,
    anotherProp : "banana",
    objInObj :{
        id : 5,
        props : "pancake"
	}
}
//a class also
class Rabbit {
    constructor(name,color,age,height,weight){
        this.name = name
        this.color = color
        this.array = [age,height,weight]
	}
    //conveting to int using map in this method
    adabtType(){
        this.array.map((e) => {
            int(e)
		}
        )
        console.log("Done")
	}
}
