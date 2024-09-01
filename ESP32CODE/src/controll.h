#include <stdint.h>

#ifndef CONTROLS
#define CONTROLS

typedef struct Rover
{
    uint8_t left_f_pwm;
    uint8_t left_f_DIR;
    uint8_t right_f_pwm;
    uint8_t right_f_DIR;
    uint8_t left_b_pwm;
    uint8_t left_b_DIR;
    uint8_t right_b_pwm;
    uint8_t right_b_DIR;

    int speed;
    int speedLimit;

} Rover;

void Forward(const Rover *rover)
{
    digitalWrite(rover->left_f_DIR, HIGH);
    digitalWrite(rover->right_f_DIR, LOW);
    digitalWrite(rover->left_b_DIR, HIGH);
    digitalWrite(rover->right_b_DIR, LOW);
}
void Backward(const Rover *rover)
{
    digitalWrite(rover->left_f_DIR, LOW);
    digitalWrite(rover->right_f_DIR, HIGH);
    digitalWrite(rover->left_b_DIR, LOW);
    digitalWrite(rover->right_b_DIR, HIGH);
}

void Right(const Rover *rover)
{
    digitalWrite(rover->left_f_DIR, HIGH);
    digitalWrite(rover->right_f_DIR, HIGH);
    digitalWrite(rover->left_b_DIR, HIGH);
    digitalWrite(rover->right_b_DIR, HIGH);
}
void Left(const Rover *rover)
{
    digitalWrite(rover->left_f_DIR, LOW);
    digitalWrite(rover->right_f_DIR, LOW);
    digitalWrite(rover->left_b_DIR, LOW);
    digitalWrite(rover->right_b_DIR, LOW);
}

void set_dir(String DIR, const Rover *rover)
{
    if(DIR == "FORWARD"){
        Forward(rover);
    }else if (DIR == "BACKWARD"){
        Backward(rover);
    }else if(DIR == "LEFT"){
        Left(rover);
    }else if(DIR == "RIGHT"){
        Right(rover);
    }
}
void set_speed(Rover *rover, int speed)
{
    if (speed < 0)
    {
        speed = -speed;
    }
    else if (speed > rover->speedLimit)
    {
        speed = rover->speedLimit;
    }
    rover->speed = speed;
}
void run(const Rover *rover){
    analogWrite(rover->left_b_pwm,rover->speed);
    analogWrite(rover->left_f_pwm, rover->speed);
    analogWrite(rover->right_b_pwm, rover->speed);
    analogWrite(rover->right_f_pwm, rover->speed);
}
void make_setup(const Rover *rover)
{
    pinMode(rover->left_f_pwm, OUTPUT);
    pinMode(rover->left_f_DIR, OUTPUT);
    pinMode(rover->right_f_pwm, OUTPUT);
    pinMode(rover->right_f_DIR, OUTPUT);
    pinMode(rover->left_b_pwm, OUTPUT);
    pinMode(rover->left_b_DIR, OUTPUT);
    pinMode(rover->right_b_pwm, OUTPUT);
    pinMode(rover->right_b_DIR, OUTPUT);
}
#endif