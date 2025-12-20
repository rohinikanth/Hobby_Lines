package game;
import java.util.Random;
import java.util.Scanner;


public class TicTacToe{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        //create board for palying
        char[][] board = {{' ', ' ', ' '},
                          {' ', ' ', ' '},
                          {' ', ' ', ' '}};
        printBoard(board);
        
        
        while(true){
            playerTurn(board,scanner);
            if (isGameFinished(board)){
        
                break;
            }
            printBoard(board);
            computerTurn(board);
            
            if (isGameFinished(board)){ 
                break;
            }
            printBoard(board);
        }
        scanner.close();

    }


    private static void printBoard(char[][] board){
        //System.out.println("________");
        System.out.println("|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|");
        System.out.println("-+-+-+-+-");
        System.out.println("|" +board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" );
        System.out.println("-+-+-+-+-");
        System.out.println("|" +board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|");
        //System.out.println("________");
    }
    

    private static boolean isSpaceAvailable(char[][] board, String pos){
            switch(pos){
                case "1": return  (board[0][0]==' ');
                case "2": return  (board[0][1]==' '); 
                case "3": return  (board[0][2]==' '); 
                case "4": return  (board[1][0]==' '); 
                case "5": return  (board[1][1]==' ');
                case "6": return  (board[1][2]==' ');
                case "7": return  (board[2][0]==' '); 
                case "8": return  (board[2][1]==' ');
                case "9": return  (board[2][2]==' ');
                default : return false;
        }
    }

    public static boolean whoWon(char[][] board, char sym){   //Winning case
        if ( (board[0][0]== sym && board[0][1]==sym && board[0][2]== sym ) ||
             (board[1][0]== sym && board[1][1]== sym && board[1][2]== sym ) ||
             (board[2][0]== sym && board[2][1]== sym && board[2][2]== sym ) ||
             (board[0][0]== sym && board[1][0]== sym && board[2][0]== sym ) ||
             (board[0][1]== sym && board[1][1]== sym && board[2][1]== sym ) ||
             (board[0][2]== sym && board[1][2]== sym && board[2][2]== sym ) ||
             (board[0][0]== sym && board[1][1]== sym && board[2][2]== sym ) ||
             (board[0][2]== sym && board[1][1]== sym && board[2][0]== sym )  )
        { 
             return true;
             }
             return false;

    }

    public static boolean isGameFinished(char[][] board) {

        if (whoWon(board, 'X')){
            
            printBoard(board);
            System.out.println("Hoorary Player wins!");
            return true;
        }

        if (whoWon(board, 'O')){
          
           printBoard(board);
           System.out.println("Hoorary Computer wins!");
           return true;
        }

       for (int i=0;i<board.length;i++){
            for(int j=0;j<board[i].length;j++){
               if (board[i][j]==' '){
                return false;
               }
            }
        }
        System.out.println("The game ended on tie!");
        printBoard(board);
        return true;
    }

    private static void placeMove(char[][] board,String position, char sym){   //method able to be  useed by both comp and palyer    
        switch(position){
            case "1": board[0][0]=sym;
                      break;   
            case "2": board[0][1]=sym;
                      break;   
            case "3": board[0][2]=sym;
                      break; 
            case "4": board[1][0]=sym;;
                      break;   
            case "5": board[1][1]=sym;;
                      break;   
            case "6": board[1][2]=sym;
                      break;
            case "7": board[2][0]=sym;
                      break;   
            case "8": board[2][1]=sym;
                      break;   
            case "9": board[2][2]=sym;
                      break;   
            default : System.out.println("Invalid choice");
        }
    }

    public static void playerTurn(char[][] board,Scanner scanner){

        while(true){
            System.out.println("Where would you like to play(1-9)?");
            String userInput = scanner.nextLine();
            if (isSpaceAvailable(board,userInput)) {
                
                placeMove(board,userInput, 'X');
                break;
            }
            else{
                System.out.println("Position already taken. Choose another.");
            }
        }   
    }


    public static void computerTurn(char[][] board){

        int compMove;
        Random rand = new Random();  //So the computer needs to pick some random spot
            while(true){
                compMove = rand.nextInt(9) + 1 ;//random int b/w 0 and 8

                if (isSpaceAvailable(board,Integer.toString(compMove))) {
                    System.out.println("computer choose: " + compMove);
                    placeMove(board, Integer.toString(compMove), 'O');
                    
                    break;
                }
                
                   
            }
                
                
    }
   
} 