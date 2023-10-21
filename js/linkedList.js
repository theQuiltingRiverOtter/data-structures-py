const {Node} = require("./node.js")

class LinkedList {
    constructor(){
        this.head  = null
        this.tail = null
        this.length = 0
    }

    push(value){
        let node = new Node(value)
        if (this.head == null) {
           this.head = node
           this.tail = node
        }
        else {
            this.tail.next =  node;
            this.tail = node
        }
        this.length++;
        return this
    }
    pop(){
        if (this.head == null) return undefined;
        let current = this.head;
        let newTail = current
        while (current.next){
            newTail = current
            current = current.next
        }

        this.tail = newTail
        this.tail.next = null
        this.length--;
        if(this.length === 0){
            this.head = null;
            this.tail = null;
        }
        return current

    }
    shift(){
        if (!this.head) return null;
        let currentHead = this.head;
        this.head = currentHead.next
        currentHead.next = null
        this.length--;
        if (this.length === 0){
            this.tail = null;
        }
        return currentHead

    }
    unshift(value){
        let node = new Node(value);
        if (!this.head){
            this.head = node;
            this.tail = this.head;
        } else {
        node.next = this.head;
        this.head = node
        }
        this.length++;
        
    }
    get(i){
        if (i >= this.length || i < 0) return null;
        let current = this.head;
        for (let j = 0; j < i; j++){
            current = current.next
        }
        return current
    }
    set(i, value){
        let foundNode = this.get(i);
        if (foundNode){
            foundNode.value = value;
            return true;
        }
        return false;
    }
    insert(i, value){
        if (i < 0 || i > this.length) return undefined;
        else if (i === 0) this.unshift(value);
        else if (i === this.length) this.push(value);
        else {
            let node = new Node(value);
            let prevNode = this.get(i-1);
            let temp = prevNode.next
            prevNode.next = node
            node.next = temp
            this.length++;
        }
    }
    remove(i){
        if (i < 0 || i > this.length) return undefined;
        if (i === 0) return this.shift();
        if (i === this.length) return this.pop();
        let prevNode = this.get(i-1)
        let removed = prevNode.next
        prevNode.next = prevNode.next.next
        this.length--;
        removed.next = null
        return removed;
    }
    reverse(){
        if (this.head == null) return null;
        let node = this.head
        this.head = this.tail
        this.tail = node
        let prev = null;
        let next;
        for (let i = 0; i < this.length; i++){
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
    }
    static insertNodes(values, linkedList){
        for (let i = 0; i < values.length; i++){
            linkedList.push(values[i])
        }
    }
}

new_list = new LinkedList();
LinkedList.insertNodes([1,2,3,4,5,6,7,8,9,10], new_list)
new_list.unshift(100)
new_list.unshift(200)
new_list.reverse();
console.log(new_list)

