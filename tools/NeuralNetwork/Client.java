import java.net.*;
import java.io.*;
import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

import java.util.concurrent.TimeUnit;

class Client extends Thread{

    private Socket clientSocket;
    private BufferedReader inputS;
    private PrintWriter outS;
    private NeuralNetwork nn;

    private int NumOfCharities;

    //Arrays for values and corresponding normalized value
    private int[] inputID;
    private double[] normID;

    private int[] inputDOW;
    private double[] normDOW;

    private int[] inputTOI;
    private double[] normTOI;

    private int[] inputLOC;
    private double[] normLOC;

    private int[] inputMON;
    private double[] normMON;

    private int[] inputWEA;
    private double[] normWEA;



    //randomly generated id's for charities
    private int[] charID;
    private double[] charIDR;

    Client(Socket clientSocket, BufferedReader inputS,  PrintWriter outS, NeuralNetwork nn){

        this.clientSocket = clientSocket;
        this.inputS = inputS;
        this.outS = outS;
        this.nn = nn;

        this.NumOfCharities = 0;

        try{

            BufferedReader brCount = new BufferedReader(new FileReader(new File("normalizedVal.txt")));

            String line;

            //Count the number of charities

            while((line = brCount.readLine()) != null){

                this.NumOfCharities++;

            }


                //Vals for ID
                this.inputID = new int[this.NumOfCharities];
                this.normID = new double[this.NumOfCharities];

                int i = 0;

                BufferedReader br = new BufferedReader(new FileReader(new File("normalizedOrgID.txt")));

                while((line = br.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputID[i] = Integer.parseInt(split[0]);
                    this.normID[i] = Double.parseDouble(split[1]);

                    i++;

                }


                //Vals for Day of week
                i = 0;
            
                this.inputDOW = new int[7];
                this.normDOW = new double[7];

                BufferedReader brID = new BufferedReader(new FileReader(new File("normalizedDOW.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputDOW[i] = Integer.parseInt(split[0]);
                    this.normDOW[i] = Double.parseDouble(split[1]);

                    i++;

                }

                //Vals for Type of item
                i = 0;
            
                this.inputTOI = new int[7];
                this.normTOI = new double[7];

                BufferedReader brID = new BufferedReader(new FileReader(new File("normalizedTOI.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputTOI[i] = Integer.parseInt(split[0]);
                    this.normTOI[i] = Double.parseDouble(split[1]);

                    i++;

                }

                //Vals for location
                i = 0;
            
                this.inputLOC = new int[6];
                this.normLOC = new double[6];

                BufferedReader brID = new BufferedReader(new FileReader(new File("normalizedLOC.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputLOC[i] = Integer.parseInt(split[0]);
                    this.normLOC[i] = Double.parseDouble(split[1]);

                    i++;

                }

                //Vals for Month
                i = 0;
            
                this.inputMON = new int[12];
                this.normMON = new double[12];

                BufferedReader brID = new BufferedReader(new FileReader(new File("normalizedMON.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputMON[i] = Integer.parseInt(split[0]);
                    this.normMON[i] = Double.parseDouble(split[1]);

                    i++;

                }

                //Vals for weather
                i = 0;
            
                this.inputWEA = new int[3];
                this.normWEA = new double[3];

                BufferedReader brID = new BufferedReader(new FileReader(new File("normalizedMON.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.inputWEA[i] = Integer.parseInt(split[0]);
                    this.normWEA[i] = Double.parseDouble(split[1]);

                    i++;

                }

                //Random id's generated for charities
                i = 0;
            
                this.charID = new int[20];
                this.charIDR = new double[20];

                BufferedReader brID = new BufferedReader(new FileReader(new File("charID.txt")));

                while((line = brID.readLine()) != null){

                    String[] split = line.split(",");

                    this.charID[i] = Integer.parseInt(split[0]);
                    this.charIDR[i] = Double.parseDouble(split[1]);

                    i++;

                }



        }
        catch(Exception e){}


    }

    double getNormVal(int input, char type){

        switch(type){
            case 'a':
                for(int i=0; i<inputID.length; i++){
                    if(inputID[i] == input){
                        return this.normID[i];
                    }
                }
                break;

            case 'b':
                for(int i=0; i<inputDOW.length; i++){
                    if(inputDOW[i] == input){
                        return this.normDOW[i];
                    }
                }
                break;

            case 'c':
                for(int i=0; i<inputTOI.length; i++){
                    if(inputTOI[i] == input){
                        return this.normTOI[i];
                    }
                }
                break;

            case 'd':
                for(int i=0; i<inputLOC.length; i++){
                    if(inputLOC[i] == input){
                        return this.normLOC[i];
                    }
                }
                break;

            case 'e':
                for(int i=0; i<inputID.length; i++){
                    if(inputID[i] == input){
                        return this.normID[i];
                    }
                }
                break;
            

        }

        for(int i=0; i<this.NumOfCharities; i++){

            if(this.input[i] == input){
                return this.normInput[i];
            }
        }

        return 0;
    }

    double getCharRID(int input){

        for(int i=0; i<this.NumOfCharities; i++){

            if(this.charID[i] == input){
                return this.charIDR[i];
            }
        }

        return 0;
    }

        
    

    @Override
    public void run(){

            try{

                System.out.println("New thread created");

                //Client will send date, type of item, location of donation

                String inMessage = this.inputS.readLine();

                System.out.println(inMessage);

                    //remove GET /
                    String[] split = inMessage.split("/");
                    inMessage = split[1];

                    //remove HTTP
                    split = inMessage.split(" ");
                    inMessage = split[0];

                    //split three values
                    split = inMessage.split(",");

                //Get the day of the week from the date
                String dateString = "2022-"+split[0];
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
                LocalDate dateT = LocalDate.parse(dateString, formatter);
                double dayOfWeek = dateT.getDayOfWeek().getValue();

                //Get the item Type
                double itemType = Double.parseDouble(split[1]);

                //Get the location
                double location = Double.parseDouble(split[2]);


                for(int i=1; i<21; i++){

                    System.out.println(i+","+dayOfWeek+","+itemType+","+location+","+1+","+1);
                    System.out.println(getCharRID(i)+","+getNormVal((int)dayOfWeek)+","+getNormVal((int)itemType)+","+getNormVal((int)location)+","+getNormVal(1)+","+getNormVal(1));

                    double[] inVals = new double[]{getCharRID(i),getNormVal((int)dayOfWeek),getNormVal((int)itemType),getNormVal((int)location),getNormVal(1),getNormVal(1)};
                    List<Double>output = nn.predict(inVals);
                    System.out.println(i + ": " + output.toString());

                }

                //List<Double>output = nn.predict(inVals);

                /*try{ TimeUnit.SECONDS.sleep(10);}
                catch(Exception e){}*/

                //System.out.println(output.toString());

                outS.println("HTTP/1.1 200 OK\n"+
                        "Content-Type: application/json\n\n"+
                        "{"+'"'+"success"+'"'+":" + '"'+"true"+'"'+"}");

                clientSocket.close();

            }
            catch(Exception e){System.out.println(e);}

            return;

    }
}