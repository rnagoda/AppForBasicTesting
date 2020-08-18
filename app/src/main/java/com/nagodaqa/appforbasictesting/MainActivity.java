package com.nagodaqa.appforbasictesting;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.text.SpannableStringBuilder;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button button_001;
    private Button button_002;
    private Button button_003;
    private TextView textView_002;
    private TextView warningText;
    private Integer currentNumber;
    private Editable newText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button_001 = (Button) findViewById(R.id.button_001);
        button_002 = (Button) findViewById(R.id.button_002);
        button_003 = (Button) findViewById(R.id.button_003);
        textView_002 = (TextView) findViewById(R.id.textView_002);
        warningText = (TextView) findViewById(R.id.warningText);

        currentNumber = 0;
        warningText.setText("");

        button_001.setOnClickListener(this);
        button_002.setOnClickListener(this);
        button_003.setOnClickListener(this);
    }

    @Override
    public void onClick(View view)
    {
        switch (view.getId()) {
            case R.id.button_001:
                if (currentNumber < 10) {
                    currentNumber++;
                    warningText.setText("");
                }
                else
                    { warningText.setText("WARNING: Maximum Value is 10"); }
                break;

            case R.id.button_002:
                if (currentNumber > 0) {
                    currentNumber--;
                    warningText.setText("");
                }
                else
                    { warningText.setText("WARNING: Minimum Value is 0"); }
                break;

            case R.id.button_003:
                currentNumber = 0;
                break;
        }

        newText = new SpannableStringBuilder("- " + currentNumber.toString() + " -");
        textView_002.setText(newText);
    }
}