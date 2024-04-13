#include <iostream>
#include <string>
using namespace std;

string encrypt_decrypt(string textplain, int k){
    string res= "";
    for(int i = 0; i < textplain.size(); ++i){
        if (textplain[i] == ' ') res += ' ';
        else if(isupper(textplain[i])){
            res += char(int(textplain[i]  + k - 65) % 26 + 65);
        }   
        else res += char(int(textplain[i]   + k - 97) % 26 + 97); 
    }
    return res;
} 

int main(){
    string textplain;   cout << "Textplain: ";   getline(cin, textplain);
    int shift = 13;

    string Ciphertext = encrypt_decrypt(textplain, shift);
    cout    <<  "Ciphertext: "  <<  Ciphertext <<   "\n";
    cout    <<  "Decrypt: "     <<  encrypt_decrypt(Ciphertext, 26 - shift);
    
    return 0;
}
