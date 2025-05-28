// week15_3_zongzi_for_loop_array_Part2
PImage zongzi; //模仿week10
void setup(){
  size(600,400); //模仿 week04
  zongzi = loadImage("zongzi.png");
  imageMode(CENTER); //畫圖時,用正中心座標
}
float []x = new float[100]; //模仿week06
float []y = new float[100];
int N = 0; //現在有幾顆粽子要畫?
void draw(){
  background(#C0ffee); //模仿week 04
  for(int i=0; i<N; i++){
   image(zongzi, x[i], y[i], 60, 50);
    y[i]++; //粽子會往下掉
  }
}
void mousePressed(){
  x[N] = mouseX;
  y[N] = mouseY;
  N++;
}
