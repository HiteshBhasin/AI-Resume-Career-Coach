import React, {useState} from "react";

const App = ()=>{
    const [selectFile, setSelectFile] = useState(null);

    const onFileChange = async (e)=>{
        setSelectFile(e.target.files[0])
   
    const formData = new FormData();
    formData.append("Resume", selectFile, selectFile.name);

    await  fetch ("",{
        method:"POST",
        body: formData
    });
    };   
//    call is asynchronous, so selectFile may not be updated immediately when it is used to append to FormData. Instead, 
// you should use the file directly from the event. Finally

    return(
        <div>
            <input type="File" onChange={onFileChange}/>
        </div>
    )
 };
export default App

