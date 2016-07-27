#include <cstdio>
#include <climits>

// ========================================
// Создаётся список размера <size>,
// после чего происходит его перепаковка.
// ========================================

class Node {
public:

    ~Node() {
    }

    int data;
    Node *next;
};

class List {
private:
    Node *first;
    int size;
public:

    List() {
        first = NULL;
        size = 0;
    }

    int pop();

    void push(int value);

    void print();

    void repacking();

    void insert(unsigned n, int val);
};

int List::pop() {
    int result;
    if (first == NULL) return INT_MAX;


    Node *prev, *idxNode = first;
    while (idxNode->next != NULL) {
        prev = idxNode;
        idxNode = idxNode->next;
    }
    result = idxNode->data;
    prev->next = NULL;
    size--;
    return result;
}

void List::push(int value) {
    Node *newNode = new Node;
    newNode->data = value;
    if (first == NULL) {
        newNode->next = NULL;
        first = newNode;
    } else {
        newNode->next = first;
        first = newNode;
    }
    size++;
}

void List::insert(unsigned index, int value) {
    if (first == NULL) return;

    Node *idxNode = first;
    unsigned count = 0;
    while (count < index && idxNode->next != NULL) {
        count++;
        idxNode = idxNode->next;
    }
    if (count < index) return;

    Node *newNode = new Node;
    newNode->next = (idxNode->next != NULL) ? idxNode->next : NULL;
    newNode->data = idxNode->data;
    idxNode->data = value;
    idxNode->next = newNode;
    size++;
}

void List::print() {
    if (first == NULL) return;
    Node *newNode = first;
    do {
        printf("%d ", newNode->data);
        newNode = newNode->next;
    } while (newNode != NULL);
    printf("\n");
}

void List::repacking() {
    int size = (this->size % 2 == 0) ? this->size - 1 : this->size;
    for (int index = 1; index < size; index += 2) {
        int pop = this->pop();
        if (pop == INT_MAX) return;
        this->insert(index, pop);
    }
}

int main() {
    List li;
    int size = 50;
    for (int i = 0; i < size; ++i) {
        li.push(i);
    }
    li.print();
    li.repacking();
    li.print();
    return 0;
}