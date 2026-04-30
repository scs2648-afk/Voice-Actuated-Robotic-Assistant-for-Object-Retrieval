#include
#include
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
void smoothMove(int channel, int start, int end, int speed) {
if (start < end) {
for (int i = start; i <= end; i++) {
pwm.setPWM(channel, 0, map(i, 0, 180, 150, 600));
delay(speed);
}
} else {
for (int i = start; i >= end; i--) {
pwm.setPWM(channel, 0, map(i, 0, 180, 150, 600));
delay(speed);
}
}
}
void executePickPlace(int pickupAngle, int gripAngle) {
smoothMove(3, 0, 90, 10);
smoothMove(0, 90, pickupAngle, 20);
smoothMove(1, 90, 140, 10);
smoothMove(2, 90, 31, 10);
delay(800);
smoothMove(3, 90, gripAngle, 20);
delay(1200);
smoothMove(2, 31, 85, 10);
smoothMove(1, 140, 100, 10);
smoothMove(0, pickupAngle, 150, 25);
smoothMove(1, 100, 140, 10);
smoothMove(2, 85, 31, 10);
delay(800);
smoothMove(3, gripAngle, 90, 20);
delay(500);
smoothMove(2, 31, 90, 10);
smoothMove(1, 140, 90, 10);
smoothMove(3, 90, 0, 20);

smoothMove(0, 150, 90, 20);
}
void setup() {
Serial.begin(9600);
pwm.begin();
pwm.setPWMFreq(60);
Serial.println("Voice Controlled Arm Ready.");
}
void loop() {
if (Serial.available() > 0) {
char cmd = Serial.read();
if (cmd == 'M' || cmd == 'm') executePickPlace(20, 5);
if (cmd == 'B' || cmd == 'b') executePickPlace(50, 22);
}
}