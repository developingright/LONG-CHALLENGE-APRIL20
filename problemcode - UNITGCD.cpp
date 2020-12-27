#include<iostream>
using namespace std;

#define ll long long

int main(){
    int t;cin>>t;
    ll int n;
    while(t--){
        cin>>n;
        if (n==1){
            cout<<"1\n1 1\n";
            continue;
        }
        cout<<(n/2)<<"\n";

        if(n%2==0){

            for(int i=2;i<=n;i+=2){
                cout<<"2 "<<i-1<<" "<<i<<"\n";
            }

        }
        else{
            cout<<"3 1 2 " << n <<"\n";
            for (int i=4;i<=n-1;i+=2){
                cout<<"2 "<< i-1 << " " << i << "\n";
            }

        }

    }

    return 0;
}