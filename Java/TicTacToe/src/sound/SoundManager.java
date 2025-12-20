package sound;
import javax.sound.sampled.*;
import java.io.File;

public class SoundManager {

    private static Clip clip;

    private static void playSound(String fileName) {
        try {
            if (clip != null && clip.isRunning()) {
                clip.stop();
                clip.close();
            }

            File file = new File("sounds/" + fileName);
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(file);

            clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.start();

        } catch (Exception e) {
            System.out.println("Sound error: " + fileName);
        }
    }

    // Convenience methods
    public static void playerMove() {
        playSound("click.wav");
    }

    public static void computerMove() {
        playSound("click.wav");
    }

    public static void win() {
        playSound("win.wav");
    }

    public static void draw() {
        playSound("draw.wav");
    }
} 
