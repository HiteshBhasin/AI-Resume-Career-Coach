import React, {useState} from "react";

const App = ()=>{
    const [selectFile, setSelectFile] = useState(null);
    const onFileChange = (e)=>{
        setSelectFile(e.target.file[0])
    }
    const formData = new FormData();
    formData.append("Resume", selectFile, selectFile.name);


}
