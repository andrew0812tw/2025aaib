// week13_5_sound 要播放音樂
// 要先安裝 Sketch-Library-Manage Libraries...
// 找sound 下載 Sound 的函式 點Install安裝完
import processing.sound. *; //使用聲音的外掛
SoundFile mySound; //宣告變數 mySound 它是 SoundFile
void setup(){
  size(400,400); //視窗大小 400*400 小心,檔名的空白
  //記得要先把音樂檔 "Intro Sound_Final.mp3" 拉到程式裡
  mySound = new SoundFile(this, "Intro Song_final.mp3");
  mySound.play(); //再播放剛剛讀入的聲音檔
}
void draw(){

} //裡面是空的畫圖,要寫它
