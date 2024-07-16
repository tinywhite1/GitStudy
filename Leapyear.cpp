#include <iostream>
using namespace std;

bool isLeapyear(int n){
    if(n%4==0&&n%100!=0||n%400==0)
    return 1;
    else return 0;
}
int main() {
    int n;
    cout << "请输入年份"<<endl;
    cin >> n;
    if(isLeapyear(n))
    cout <<"是闰年"<< endl;
    else cout <<"不是闰年"<<endl;
    return 0;
}