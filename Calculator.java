import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Calculator extends JFrame implements ActionListener {
    private JTextField display;
    private String operator = "";
    private double firstNumber = 0, secondNumber = 0, result = 0;
    private boolean startNewNumber = true;

    // Constructor
    public Calculator() {
        setTitle("Calculator");
        setSize(300, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Display
        display = new JTextField();
        display.setFont(new Font("Arial", Font.BOLD, 20));
        display.setHorizontalAlignment(JTextField.RIGHT);
        display.setEditable(false);
        add(display, BorderLayout.NORTH);

        // Buttons
        String[][] buttonLabels = {
            {"AC", "BKSP", "+/-", "/"},
            {"7", "8", "9", "x"},
            {"4", "5", "6", "-"},
            {"1", "2", "3", "+"},
            {"%", "0", ".", "="}
        };

        JPanel buttonPanel = new JPanel(new GridLayout(5, 4, 5, 5));

        for (String[] row : buttonLabels) {
            for (String text : row) {
                JButton button = new JButton(text);
                button.setFont(new Font("Arial", Font.BOLD, 16));
                button.addActionListener(this);
                buttonPanel.add(button);
            }
        }

        add(buttonPanel, BorderLayout.CENTER);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (command.matches("[0-9]") || command.equals(".")) {
            if (startNewNumber) {
                display.setText(command);
                startNewNumber = false;
            } else {
                display.setText(display.getText() + command);
            }
        } else if (command.equals("AC")) {
            display.setText("");
            operator = "";
            firstNumber = secondNumber = result = 0;
            startNewNumber = true;
        } else if (command.equals("BKSP")) {
            String text = display.getText();
            if (text.length() > 0) {
                display.setText(text.substring(0, text.length() - 1));
            }
        } else if (command.equals("+/-")) {
            String text = display.getText();
            if (!text.isEmpty()) {
                double value = Double.parseDouble(text);
                display.setText(String.valueOf(-value));
            }
        } else if (command.equals("%")) {
            String text = display.getText();
            if (!text.isEmpty()) {
                double value = Double.parseDouble(text);
                display.setText(String.valueOf(value / 100));
            }
        } else if (command.equals("=")) {
            if (!operator.isEmpty()) {
                secondNumber = Double.parseDouble(display.getText());
                switch (operator) {
                    case "+" -> result = firstNumber + secondNumber;
                    case "-" -> result = firstNumber - secondNumber;
                    case "x" -> result = firstNumber * secondNumber;
                    case "/" -> result = firstNumber / secondNumber;
                }
                display.setText(String.valueOf(result));
                operator = "";
                startNewNumber = true;
            }
        } else { // Operators
            firstNumber = Double.parseDouble(display.getText());
            operator = command;
            startNewNumber = true;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Calculator().setVisible(true);
        });
    }
}

