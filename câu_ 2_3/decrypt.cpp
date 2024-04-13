#include <iostream>
#include <string>
using namespace std;

string decrypt(string ciphertext, int k){
    string res = "";
    for(int i = 0; i < ciphertext.size(); ++i){
        if (ciphertext[i] == ' ') res += ' ';
        else if(isupper(ciphertext[i])){
            res += char(int(ciphertext[i] + k - 65) % 26 + 65);
        }
        else res += char(int(ciphertext[i] + k - 97) % 26 + 97);
    }
    return res;
} 

int main(){
    string ciphertext;   cout << "Ciphertext: ";   getline(cin, ciphertext);
    for (int k = 1; k <= 25; ++k) {
        cout << "Shift = " << k << ": ";
        cout << decrypt(ciphertext, 26 - k) << endl;
    }
    return 0;
}
