#define BEGINPIN 22
#define ENDPIN 53
#define DEBOUNCING 350

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

byte saklar = 0;
byte kamar[] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
  Serial.begin(1200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  for (byte i = 0; i <= sizeof(kamar); i++)
  {
    pinMode(kamar[i], OUTPUT);
    digitalWrite(kamar[i], HIGH);

  }
  for (byte i = BEGINPIN; i <= ENDPIN; i++)
  {
    digitalWrite(i, HIGH);
    pinMode(i, INPUT_PULLUP);
  }
  // put your setup code here, to run once:

}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    //Serial.println(inputString);
	
	//Req: AT
	if (inputString[0] == 'A' && inputString[1] == 'T'){
      Serial.println("OK");
	}
	
	//Req: L? ---> Num ? Turn ON (Low Signal)
    else if (inputString[0] == 'L') {
      //Serial.println("ON");
      byte num = inputString[1] - 0x31;
      //Serial.println(num, DEC);
      if (num < sizeof(kamar) && num >= 0) {
        //Serial.println(kamar[num], DEC);
        digitalWrite(kamar[num], LOW);
        Serial.print("A"); //SA --> Acknowledge
        Serial.println(inputString[1]); 
      } else {
        Serial.println("EO"); //EO --> Error Overflow pin number
      }
    }
	
	//Req: H? ---> Num ? Turn OFF (High Signal)
    else if (inputString[0] == 'H') {
      //Serial.println("OFF");
      byte num = inputString[1] - 0x31;
      Serial.println(num, DEC);
      if (num < sizeof(kamar) && num >= 0) {
        //Serial.println(kamar[num], DEC);
        digitalWrite(kamar[num], HIGH);
        Serial.print("A"); //SA --> Acknowledge
        Serial.println(inputString[1]); 
      } else {
        Serial.println("EO");
      }
    }
	
	else
		Serial.println("NA");  //NA --> Not Acknowledge
	
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
  
  //baca pin --> Rx		Request number x
  for (byte i = BEGINPIN; i <= ENDPIN; i++)
  {
    digitalWrite(i, HIGH);
    if (!digitalRead(i)) {
      delay(DEBOUNCING);
      saklar = i - BEGINPIN;
      Serial.print("R");
      Serial.write(saklar+0x30);
      Serial.println();
    }
  }

}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
