#include <controlls.h>

Rover rover = {
        .left_f_pwm = 2,
        .left_f_DIR = 22,
        .right_f_pwm = 3,
        .right_f_DIR = 23,
        .left_b_pwm = 4,
        .left_b_DIR = 24,
        .right_b_pwm = 5,
        .right_b_DIR = 25,
        .speed = 10,
        .speedLimit = 200
    };

void setup(){
  Serial.begin(9600);
  make_setup(&rover);
}

void loop() {
  if(Serial.available()>0){
    println(Serial.read())
  }
  Forward(&rover);
  set_speed(&rover, 50);

}