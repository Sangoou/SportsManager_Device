package data;

public class Game {

    private String TeamA, TeamB;
    private int scoreA, scoreB;
    private int setScoreA, setScoreB;
    private int scoreForWin, setScoreForWin;

    public Game(String TeamA, String TeamB, int scoreForWin, int setScoreForWin) {
        this.TeamA = TeamA;
        this.TeamB = TeamB;
        this.scoreForWin = scoreForWin;
        this.setScoreForWin = setScoreForWin;
        initGame();
    }

    public void initGame() {
        scoreA = 0;
        scoreB = 0;
        setScoreA = 0;
        setScoreB = 0;
    }

    public Boolean increaseScoreA() {
        if(scoreA >= scoreForWin){
            return false;
        }
        scoreA = scoreA + 1;
        return true;
    }

    public Boolean decreaseScoreA() {
        if(scoreA <= 0){
            return false;
        }
        scoreA = scoreA - 1;
        return true;
    }

    public Boolean increaseScoreB() {
        if(scoreB >= scoreForWin){
            return false;
        }
        scoreB = scoreB + 1;
        return true;
    }

    public Boolean decreaseScoreB() {
        if(scoreB <= 0){
            return false;
        }
        scoreB = scoreB - 1;
        return true;
    }

    public Boolean increaseSetScoreA() {
        if(setScoreA >= setScoreForWin){
            return false;
        }
        setScoreA = setScoreA + 1;
        scoreA = 0;
        scoreB = 0;
        return true;
    }

    public Boolean increaseSetScoreB() {
        if(setScoreB >= setScoreForWin){
            return false;
        }
        setScoreB = setScoreB + 1;
        scoreA = 0;
        scoreB = 0;
        return true;
    }

    public String getWinner() {
        String winner = null;

        if(setScoreA >= setScoreForWin){
            winner = "A";
        } else if(setScoreB >= setScoreForWin) {
            winner = "B";
        }

        return winner;
    }

    public String getSetWinner() {
        String winner = null;

        if(scoreA >= scoreForWin){
            winner = "A";
        } else if(scoreB >= scoreForWin){
            winner = "B";
        }

        return winner;
    }

    public int getScoreA() {
        return scoreA;
    }

    public int getScoreB() {
        return scoreB;
    }

    public int getSetScoreA() {
        return setScoreA;
    }

    public int getSetScoreB() {
        return setScoreB;
    }

    public int getScoreForWin() {
        return scoreForWin;
    }

    public int getSetScoreForWin() {
        return setScoreForWin;
    }
}
