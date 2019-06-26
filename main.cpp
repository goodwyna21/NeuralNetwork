#include "/home/archer/Projects/ArcherStandardLibrary/Source/all.h"
using namespace std;

#define math_e 2.71828;

/*
Symbols:
n: layer
j: neuron in layers
k: neuron in previous layer
i: sample number

a: nonlinearized activation value
z: linear activation value

q: cost function
*/

struct Network{
    vector<uint> shape;
    uint height;
    uint out_n;

    vector<vector<vector<double>>> w;
    vector<vector<double> > b;

    vector<vector<vector<double>>> data;

    Network(initializer_list<uint> structure,vector<vector<vector<double>>> training_data=vector<vector<vector<double>>>()){
        shape = structure;
        height = shape.size();
        out_n = height - 1;
    }

    Image display(){
        int maxW = 0;
        for(int n = 0; n < height; n++){
            if(shape[n] > maxW){
                maxW = shape[n];
            }
        }
        uint h;
        Image img(50*(height),50*(maxW));
        for(int n = 0; n < height; n++){
            for(int j = 0; j < shape[n]; j++){
                h=50*(j + ((maxW-shape[n])/2.0)) + 25;
                if(n > 0){
                    for(int k = 0; k < shape[n-1]; k++){
                        img.line(50*(n-1)+25,50*(k+((maxW-shape[n-1])/2.0))+25,
                                 50*n + 25,h);
                    }
                }
                img.circle(50*n + 25,h,15,{0,0,255});
            }
        }
        img.line(100,100,300,100);
        return img;
    }
};

int main(int argc, char* argv[]){
    cout << "begin\n";
/*
    Network net({3,2,4,4,1});
    cout << "1";
    Image img = net.display();
    cout << "2";
    img.savePPM("test.ppm");
*/
    Image img(400,400);
    img.text("Yeet",100,100);
    img.savePPM("test.ppm");
    cout << "done\n";
    return 0;
}
