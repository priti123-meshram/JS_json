console.log(("\n ** WELLCOME TO LOGIN SIGNUP PAGE **\n"))
let z=require("readline-sync");
var user= z.question("enter the login and signup :- ");
if (user=="signup"){
    var user1= z.question("enter user name :- ");

    var pass1= z.question("enter the password :- ");
    var pass2= z.question("enter the conform password :- ");
    if (pass1==pass2){
        console.log("your password is confirmed")
        var birth= z.questionInt("enter the birthdate :- ")
        var contactno= z.questionInt("enter the contact number :- ");
        if (contactno>1000000000 && contactno<=9999999999){
            var gender= z.question("enter the gender :- ");
            if (gender=="male" || gender=="female"){
                var hobbies= z.question("enter the hobbies :- ");
                var qualification= z.question("enter the qualification :- ");
                dict={"username":user1,"pass2":pass2,"birth":birth,"contactno":contactno,"gender":gender,"hobbies":hobbies,"qualification":qualification}
                    const fs=require('fs');
                    const file=fs.writeFileSync("text2.json",JSON.stringify(dict,null,4))
            }
            else{
                console.log(" your speling is mistek")
            }
        }
        else{
            console.log("sorry invalid number")
        }
    }
    else{
        console.log("wrong password")
    }
}
else{
    if (user=="login"){
        var usr_name= z.question("enter the user name :- ");
        var password= z.question("enter the password :- ");
        const fs=require('fs');
        var data =fs.readFileSync("text2.json")
        var data1=JSON.parse(data)
            for (i in (data1)){
                if (usr_name==data1[i]["user1"],["username"]){
                    if (password==data1[i]["pass2"],["pass2"]){
                        console.log("\n*****login successful*****\n")
                        console.log(data1)
                        break
                    }
                    else{
                        console.log("wrong password")
                    }
                }
                else{
                    console.log("user name incarect")
                }
            }
        
        
        
    }
    else{
        console.log(data1)
    }
    
}

















