const {Node} = require("./node.js")

class Stack {
    constructor(){
        this.head = null;
        this.length = 0
    }

    push(value){
        let node = new Node(value);
        let oldHead = this.head;
        this.head = node;
        this.head.next = oldHead;
        this.length++
    }

    pop(){
        if (this.head == null){
            return null
        }
        let value = this.head.value
        this.head = this.head.next
        this.length--
        return value
    }
    peek(){
        return (this.head == null) ? null : this.head.value;
    }

    size(){
        // let current = this.head
        // let count = 0
        // while (current != null){
        //     count++;
        //     current = current.next
        // }
        return this.length


    }
    is_empty() {
        return (this.head == null) ? true : false;
    }
}


function reverse_string(string1){
    let stack = new Stack();
    let new_string = "";
    for (let i = 0; i < string1.length; i++){
        stack.push(string1[i]);
    }
    let size = stack.size();
    for (let j = 0; j < size; j++){
        new_string += stack.pop();
    }
    return new_string;
}

console.log(reverse_string("hello world"))

const stack = new Stack();
console.log(stack.is_empty())
stack.push(5)
stack.push(10)
stack.push(2)
stack.push(25)
console.log(stack.is_empty())
console.log(stack.peek())
console.log(stack.size())
console.log(stack.pop())
console.log(stack)