Set WshShell = WScript.CreateObject("WScript.Shell")

 Set oWSH = CreateObject("WScript.Shell")
 vbsInterpreter = "cscript.exe"

 Call ForceConsole()

 Function printf(txt)
    WScript.StdOut.WriteLine txt
 End Function

 Function wait(n)
    WScript.Sleep Int(n * 1000)
 End Function

 Function ForceConsole()
    If InStr(LCase(WScript.FullName), vbsInterpreter) = 0 Then
        oWSH.Run vbsInterpreter & " //NoLogo " & Chr(34) & WScript.ScriptFullName & Chr(34)
        WScript.Quit
    End If
 End Function

 Function cls()
    For i = 1 To 50
        printf ""
    Next
 End Function

 printf ""
 printf " SYSTEM STARTUP SCRIPT - V0.4b (simple update point)"
 printf ""
 printf " If this script fails to run properly, please start the machines manually and then"
 printf " shutdown and retry. It's usually a case of the IP being dropped."
 printf " A manual restart should reacquire the IP address which will then link to the script"
 printf ""
   
REM WScript.Echo "Running Boot Sequence"
WshShell.Run ("git clone https://github.com/Kjarr/ts_notes.git")
WScript.sleep 2000
printf " Service Initalised..."
printf " "
WshShell.CurrentDirectory = "C:\TEST\"
wait(2)
printf " Running Boot Sequence..."
printf " "
wait(2)
WshShell.Run ("C:\TEST\ts_notes\hello.vbs")
printf " Machines should now be coming online..."
wait(1)
printf " THIS MAY TAKE A FEW SECONDS PLEASE PERFORM VISUAL CHECK"
printf " "
wait(5)
REM WScript.sleep 2000
printf " Boot Sequence Complete!"
wait(2)


WshShell.CurrentDirectory = "C:\TEST\"

strPath = "C:\TEST\ts_notes"

DeleteFolder strPath

Function DeleteFolder(strFolderPath)
Dim objFSO, objFolder
Set objFSO = CreateObject ("Scripting.FileSystemObject")
If objFSO.FolderExists(strFolderPath) Then
objFSO.DeleteFolder strFolderPath, True
End If
Set objFSO = Nothing
End Function

 WScript.Quit
