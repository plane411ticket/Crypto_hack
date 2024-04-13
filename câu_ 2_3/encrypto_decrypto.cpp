#include <iostream>
#include <string>
using namespace std;

string encrypt(string textplain){
    string res= "";

    for (int k = 1; k <= 25; ++k) {
        cout << "Shift = " << k << ": ";
        for(int i = 0; i < textplain.size(); ++i){
            if (textplain[i] == ' ') res += ' ';
            else if(isupper(textplain[i])){
                res += char(int(textplain[i]  + k - 65) % 26 + 65);
            }
            else res += char(int(textplain[i]   + k - 97) % 26 + 97);
        }
        cout << res << endl;
        res = ""; // reset chuỗi res về rỗng cho giá trị shitf kế tiếp
    }

    return res;
} 

int main(){
    string textplain;   cout << "Textplain: ";   getline(cin, textplain);
    encrypt(textplain); 
    return 0;
}
