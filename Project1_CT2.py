


def LRT() :
    Station = ["Dukuh Atas", "Setiabudi", "Rasuna Said", "Kuningan", "Pancoran",
               "Cikoko", "Ciliwung", "Cawang", "Taman Mini", "Kampung Rambutan",
               "Ciracas", "Harjamukti"]

    for i in range(0, 11) :
        Station[i]
        S = Station[i]
        print(S)

    LocationStart = input(f"Where are you now sir {Name} " )

    StationI = input(f"Where you wanna go sir {Name} ")

    Start = -1
    End = -1

    for i in range(0, 11) :
        if Station[i] == LocationStart :
            Start = i
            break

    for i in range(0, 11) :
        if Station[i] == StationI :
            End = i
            break

    if Start == -1 or End == -1 :
        print(f"Station not found, sir {Name}")
        return

    Distance = End - Start
    if Distance < 0 :
        Distance = Distance * -1

    Price = 0
    for i in range(Distance) :
        if i < 2 :
            Price += 5000
        else :
            Price += 7000

    print(f"You should pay RP.{Price}, sir {Name}")


def MRT() :
    Station = ["Kemayoran", "Pasar Senen", "Rajawali", "Gang Sentiong", "Kramat Juanda",  
                   "Sawah Besar", "Gondangdia", "Cikini Gambir", "Jayakarta" , "Jakarta Kota"]
    LocationStart = input(f"Where are you now sir {Name} " )

    StationI = input(f"Where you wanna go sir {Name} ")

    for i in range(0, 11) :
            Station[i]
            S = Station[i]
            print(S)
    
    Start = -1
    End = -1

    for i in range(0, 11) :
     if Station[i] == LocationStart :
        Start = i
        break

    for i in range(0, 11) :
        if Station[i] == StationI :
            End = i
            break

    if Start == -1 or End == -1 :
        print(f"Station not found, sir {Name}")
        return

    Distance = End - Start
    if Distance < 0 :
        Distance = Distance * -1
    Distance = Distance * 10000
    print(f"You should pay RP.{Distance}, Sir {Name}")


def KRL() :
    LocationStart = input(f"Where are you now sir {Name} " )

    StationI = input(f"Where you wanna go sir {Name} ")

    for i in range(0, 11) :
            Station[i]
            S = Station[i]
            print(S)
            
    Station = ["Kemayoran", "Pasar Senen", "Rajawali", "Gang Sentiong", "Kramat Juanda",  
                   "Sawah Besar", "Gondangdia", "Cikini Gambir", "Jayakarta" , "Jakarta Kota"]

    Start = -1
    End = -1

    for i in range(0, 11) :
     if Station[i] == LocationStart :
        Start = i
        break

    for i in range(0, 11) :
        if Station[i] == StationI :
            End = i
            break

    if Start == -1 or End == -1 :
        print(f"Station not found, sir {Name}")
        return


    Distance = End - Start
    Price = 0
    if Distance < 0 :
        Distance = Distance * -1

    while True:
        i = 0
        if i != Distance :
            if i <= 2 :
                Price += 3000
            else :
                Price += 5000
        else :
            break 
    
    print(f"You should pay RP.{Price}, Sir {Name}")



"""

string name = "";
string train = "";

int main() {
    cout << "What's your name sir? ";
    cout << "Train (MRT/KRL/LRT): ";

    if (train == "MRT") {
        MRT();
    } else if (train == "KRL") {
        KRL();
    } else if (train == "LRT") {
        LRT();
    } else {
        cout << "train not available, sir " << name << endl;
    }
    return 0;
}

void MRT() {
    string station[13] = {"Lebak Bulus", "Fatmawati", "Cipete Raya", "Haji Nawi", "Blok A",
                          "Blok M", "ASEAN", "Senayan", "Istora", "Bendungan Hilir",
                          "Setiabudi", "Dukuh Atas", "Bundaran HI"};
    string location_start = ""; string station_i = "";
    int start = -1; int end = -1; int distance = 0; int price = 0;

    cout << "MRT stations: ";
    for (int i = 0; i < 13; i++) {
        cout << station[i] << ", ";
    }
    cout << endl;

    cout << "Where are you now sir " << name << " ";
    cout << "Where you wanna go sir " << name << " ";

    for (int i = 0; i < 13; i++) {
        if (station[i] == location_start) {
            start = i;
            break;
        }
    }
    for (int i = 0; i < 13; i++) {
        if (station[i] == station_i) {
            end = i;
            break;
        }
    }

    if (start == -1 || end == -1) {
        cout << "Station not found, Sir " << name << endl;
        return;
    }

    distance = end - start;
    if (distance < 0) {
        distance = distance * -1;
    }

    for (int i = 0; i < distance; i++) {
        price += 10000;
    }

    cout << "You should pay RP." << price << ", Sir " << name << endl;
}

void KRL() {
    string station[13] = {"Jakarta Kota", "Jayakarta", "Mangga Besar", "Sawah Besar", "Juanda",
                          "Gondangdia", "Cikini", "Manggarai", "Tebet", "Cawang",
                          "Duren Kalibata", "Pasar Minggu Baru", "Pasar Minggu"};
    string location_start = ""; string station_i = "";
    int start = -1; int end = -1; int distance = 0; int price = 0;

    cout << "KRL stations: ";
    for (int i = 0; i < 13; i++) {
        cout << station[i] << ", ";
    }
    cout << endl;

    cout << "Where are you now sir " << name << " ";
    cout << "Where you wanna go sir " << name << " ";

    for (int i = 0; i < 13; i++) {
        if (station[i] == location_start) {
            start = i;
            break;
        }
    }
    for (int i = 0; i < 13; i++) {
        if (station[i] == station_i) {
            end = i;
            break;
        }
    }

    if (start == -1 || end == -1) {
        cout << "Station not found, Sir " << name << endl;
        return;
    }

    distance = end - start;
    if (distance < 0) {
        distance = distance * -1;
    }

    for (int i = 0; i < distance; i++) {
        if (i < 2) {
            price += 3000;
        } else {
            price += 5000;
        }
    }

    cout << "You should pay RP." << price << ", Sir " << name << endl;
}

void LRT() {
    string station[12] = {"Dukuh Atas", "Setiabudi", "Rasuna Said", "Kuningan", "Pancoran",
                          "Cikoko", "Ciliwung", "Cawang", "Taman Mini", "Kampung Rambutan",
                          "Ciracas", "Harjamukti"};
    string location_start = ""; string station_i = "";
    int start = -1; int end = -1; int distance = 0; int price = 0;

    cout << "LRT stations: ";
    for (int i = 0; i < 12; i++) {
        cout << station[i] << ", ";
    }
    cout << endl;

    cout << "Where are you now sir " << name << " ";
    cout << "Where you wanna go sir " << name << " ";

    for (int i = 0; i < 12; i++) {
        if (station[i] == location_start) {
            start = i;
            break;
        }
    }
    for (int i = 0; i < 12; i++) {
        if (station[i] == station_i) {
            end = i;
            break;
        }
    }

    if (start == -1 || end == -1) {
        cout << "Station not found, Sir " << name << endl;
        return;
    }

    distance = end - start;
    if (distance < 0) {
        distance = distance * -1;
    }

    for (int i = 0; i < distance; i++) {
        if (i < 2) {
            price += 5000;
        } else {
            price += 7000;
        }
    }

    cout << "You should pay RP." << price << ", Sir " << name << endl;
}


"""