class dNode {
    constructor(value=0, next=null, prev=null){
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class doubleLinkedList {
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(value){
        let node = new dNode(value);
        if (!this.head) {
            this.head = node;
            this.tail = node;
        }
        else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node

        }
        this.length++;
    }
    pop() {
        if (!this.head) return undefined;
        let temp = this.tail;
        if (this.length == 1){
            this.head = null;
            this.tail = null;
        } else {
            this.tail = temp.prev;
            this.tail.next = null;
            temp.prev = null
        }
        this.length--;
        return temp

    }
    shift() {
        if (!this.head) return undefined;
        let temp = this.head;
        if (this.length == 1) {
            this.head == null;
            this.tail == null;
        } else {
            this.head = temp.next;
            this.head.prev = null;
            temp.next = null;
        }
        this.length--;
        return temp;
    }
    unshift(value) {
        let node = new Node(value);
        if (!this.head) {
            this.head = node;
            this.tail = node;
        } else {
            this.head.prev = node
            node.next = this.head
            this.head = node
        }
        this.length++;
    }

    get(i) {
        if (i < 0 || i >= this.length) return null;
        let current;
        if (i <= this.length/2) {
            current = this.head
            for (let j = 0; j< i; j++){
                current = current.next;
            }
        } else {
            current = this.tail;
            for (let j = this.length-1; j > i; j--){
                current = current.prev
            }
        }
        return current;
    }
    set(i, value){
        let foundNode = this.get(i);
        if (foundNode) {
            foundNode.value = value;
            return true
        }
        return false;
    }
    insert(i, value){
        if (i < 0 || i > this.length) return false;
        if (i === 0) return this.unshift(value);
        if (i === this.length) return this.push(value);
    
        let node = new Node(value);
        let prevNode = this.get(i-1);
        let nextNode = prevNode.next;
        prevNode.next = node;
        node.prev = prevNode;
        node.next = nextNode;
        nextNode.prev = node;
        this.length++;
        return true;
    }

    remove(i){
        if (i < 0 || i >= this.length) return undefined;
        if (i === 0) return this.shift();
        if (i === this.length -1) return this.pop();
        let foundNode = this.get(i);
        foundNode.prev.next = foundNode.next
        foundNode.next.prev = foundNode.prev
        foundNode.prev = null
        foundNode.next = null
        this.length--;
        return foundNode;

    }
}


dLList = new doubleLinkedList();
dLList.push(5)
dLList.push(10)
dLList.push(15)
dLList.push(25)
dLList.push(35)
console.log(dLList.get(3))