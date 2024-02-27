package tp;

import javax.swing.JOptionPane;

public class MyUtil {
	public static void display(String message){
		System.out.println(message);
	}
	
	public static void displayDlg(String message){
		JOptionPane.showMessageDialog(null, message);
	}
}
