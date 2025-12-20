package ui;

import game.TicTacToe;
import sound.SoundManager;

import javax.swing.*;
import java.awt.*;

public class TicTacToeUI {
    int playerWins = 0;
    int computerWins = 0;
    int draws = 0;


    JFrame frame;
    JButton[][] buttons = new JButton[3][3];
    JButton restartButton;

    JLabel statusLabel;
    JLabel scoreLabel;


    // USE SAME BOARD
    char[][] board = {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
    };

    public TicTacToeUI() {
        frame = new JFrame("Tic Tac Toe");
        frame.setSize(450, 450);
        frame.setLayout(new BorderLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel gridPanel = new JPanel(new GridLayout(3, 3));
        JPanel topPanel = new JPanel(new GridLayout(2, 1));

        Font font = new Font("Arial", Font.BOLD, 60);

        scoreLabel = new JLabel(getScoreText(), SwingConstants.CENTER);
        statusLabel = new JLabel("Player X's Turn", SwingConstants.CENTER);

        scoreLabel.setFont(new Font("Arial", Font.PLAIN, 16));
        statusLabel.setFont(new Font("Arial", Font.BOLD, 20));

        topPanel.add(statusLabel);
        topPanel.add(scoreLabel);


        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {

                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(font);
                buttons[i][j].setFocusPainted(false);

                int r = i;
                int c = j;

                buttons[i][j].addActionListener(e -> playerMove(r, c));

                gridPanel.add(buttons[i][j]);
                
            }
        }
        
        restartButton = new JButton("Restart");
        restartButton.setFont(new Font("Arial", Font.BOLD, 18));
        restartButton.addActionListener(e -> restartGame());

        frame.add(gridPanel, BorderLayout.CENTER);
       
        frame.add(restartButton, BorderLayout.SOUTH);

        frame.add(topPanel, BorderLayout.NORTH);
        

        
        frame.setVisible(true);

    }

    private void updateStatus() {

        if (TicTacToe.whoWon(board, 'X')) {
            statusLabel.setText("🎉 Player X Wins!");
            playerWins++;
            SoundManager.win();
        } 
        else if (TicTacToe.whoWon(board, 'O')) {
            statusLabel.setText("🤖 Computer Wins!");
            computerWins++;
            SoundManager.win();
        } 
        else {
            statusLabel.setText("🤝 It's a Tie!");
            draws++;
            SoundManager.win();
        }
        scoreLabel.setText(getScoreText());
    }
    

    private void playerMove(int r, int c) {

        if (board[r][c] != ' ') return;

        //Player move first
        board[r][c] = 'X';
        SoundManager.playerMove();
        buttons[r][c].setText("X");

        //Force UI repaint
        frame.repaint();

        //Check player win
        if (TicTacToe.isGameFinished(board)) {
            updateStatus();
            endGame();
            return;
        }

        //Computer move after short delay
        Timer timer = new Timer(300, e ->{
            TicTacToe.computerTurn(board);
            SoundManager.computerMove();
            syncBoard();

            if (TicTacToe.isGameFinished(board)) {
                updateStatus();
                endGame();
            }
        });
        timer.setRepeats(false);
        timer.start();

    }

    private void syncBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] != ' ') {
                    buttons[i][j].setText(String.valueOf(board[i][j]));
                }
            }
        }
    }

    private void endGame() {
        for (JButton[] row : buttons)
            for (JButton b : row)
                b.setEnabled(false);
    }

    private void restartGame() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
                buttons[i][j].setText("");
                buttons[i][j].setEnabled(true);
            }
        }
        statusLabel.setText("Player X's Turn");

        //for restAart to be fresh tournament
        // playerWins = 0;
        // computerWins = 0;
        // draws = 0;
        // scoreLabel.setText(getScoreText());
 
    }

    private String getScoreText() {
        return "Player X: " + playerWins +
               "   Computer O: " + computerWins +
               "   Draws: " + draws;
    }
    
    
    public static void main(String[] args) {
        new TicTacToeUI();
    }
}
