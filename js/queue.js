const {Node} = require("./node.js")

class Queue {
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    enqueu(value){
        let node = new Node(value);
        this.length++;
        if (this.head == null){
            this.head = node;
            this.head.next = this.tail;
        } else if (this.tail == null){
            this.tail = node;
            this.head.next = this.tail;
        } else {
            this.tail.next = node;
            this.tail = this.tail.next;
        }
    }
    dequeue(){
        if (this.head == null){
            return null;
        }
        let value = this.head.value;
        this.head = this.head.next;
        this.length--;
        if (this.head == null){
            this.tail = null
        }
        return value;
    }
    size(){
        return this.length;
    }

    peek(){
        return (this.head == null) ? null : this.head.value;
    }
    is_empty(){
        return this.head == null;
    }

}

let my_queue = new Queue();
my_queue.enqueu(5)
my_queue.enqueu(7)
my_queue.enqueu(10)
console.log(my_queue.peek())
my_queue.enqueu(15)
console.log(my_queue.dequeue())
console.log(my_queue.dequeue())
console.log(my_queue.dequeue())
console.log(my_queue.is_empty())
console.log(my_queue.dequeue())
console.log(my_queue.is_empty())
console.log(my_queue)
console.log(my_queue.size())