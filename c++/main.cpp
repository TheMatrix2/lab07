#include <iostream>
#include <random>

int random(int a, int b){
    return a + rand() % (b - a + 1);
}

int main(){
    srand(static_cast<unsigned int>(time(nullptr)));
    std::cout << "Hello, world! " << random(1, 100);
}