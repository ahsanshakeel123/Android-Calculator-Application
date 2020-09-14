public class MainActivity extends AppCompatActivity {
    button bnzero,bnone,bntwo bnthree, bnfive, bnsix, bnseven, bneight, bnnine, bnadd, bnsub, bnmul, bndiv,bnequal,bnclear
     TextView input;
     TextView pro;
     char Add = '+';
      char Subst = '-';
      char Mul = '*';
      char Div = '/';
     char Equation = 0;
     double num1;
     double num2;
     char SAT;
    void setupUIViews(){

        bnone = (Button)findViewById(R.id.btn1);
        bnzero = (Button)findViewById(R.id.btn0);
        bntwo = (Button)findViewById(R.id.btn2);
        bnthree = (Button)findViewById(R.id.btn3);
        bnfour = (Button)findViewById(R.id.btn4);
        bnfive = (Button)findViewById(R.id.btn5);
        bnsix = (Button)findViewById(R.id.btn6);
        bnseven = (Button)findViewById(R.id.btn7);
        bneight = (Button)findViewById(R.id.btn8);
        bnnine = (Button)findViewById(R.id.btn9);
        Add = (Button)findViewById(R.id.btnadd);
        Sub = (Button)findViewById(R.id.btnsub);
        Mul = (Button)findViewById(R.id.btnmul);
        Div = (Button)findViewById(R.id.btndivide);
        Equation = (Button)findViewById(R.id.btnequal);
        Input = (TextView)findViewById(R.id.tvinput);
        pro = (TextView)findViewById(R.id.tvResult);

    }


    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setupUIViews();

        bnzero.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "0");
            }
        });

        bnone.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "1");
            }
        });

        bntwo.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "2");
            }
        });

        bnthree.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "3");
            }
        });

        bnfour.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                input.setText(input.getText().toString() + "4");
            }
        });

        bnfive.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "5");
            }
        });

        bnsix.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "6");
            }
        });

        bnseven.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "7");
            }
        });

        bneight.setOnClickListener(new View.OnClickListener() {
                        public void onClick(View v) {
                input.setText(input.getText().toString() + "8");
            }
        });

        bnnine.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                input.setText(input.getText().toString() + "9");
            }
        });

        sub.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                calculate();
                SAT = Subst;
                pro.setText(String.valueOf(num1) + "-");
                input.setText(null);
            }
        });

        Add.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                calculate();
                SAT = Add;
                pro.setText(String.valueOf(num1) + "+");
                input.setText(null);
            }
        });

        Mul.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate();
                 SAT= Mul;
                pro.setText(String.valueOf(num1) + "*");
                input.setText(null);
            }
        });

        Div.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate();
                SAT = Div;
                pro.setText(String.valueOf(num1) + "/");
                input.setText(null);
            }
        });

        equal.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                calculate();
                SAT = Equation;
                pro.setText(result.getText().toString() + String.valueOf(num2) + "=" + String.valueOf(num1));
                // 5 + 4 = 9
                input.setText(null);
            }
        });



    void calculate(){
        if(!Double.isNaN(num1)){
            num2 = Double.parseDouble(info.getText().toString());

            switch(SAT){
                case Add:
                num1 = num1 + num2;
                break;
                case Subs:
                num1 = num1 - num2;
                break;
                case Muti:
                num1 = num1 * num2;
                break;
                case Div:
                num1 = num1 / num2;
                break
            }
        }
        else{
            num1 = Double.parseDouble(input.getText().toString());
        }
    }
}