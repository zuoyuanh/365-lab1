# 365-lab1

Requirement NR1. Given a classroom number, list all students assigned to it.
---
`Command : C[lass]: <number>`
`Example : C:102`


Requirement NR2. Given a classroom number, find the teacher (or teachers) teaching in it1.
---
`Command : C[lass]:  <number> T[eacher]`
`Example : C: 102 Teacher`

Requirement NR3. Given a grade, find all teachers who teach it. 
---
`Command : G[rade]: <number> T[eacher]`
`Example : G:  6 T`

Requirement NR4. Report the enrollments broken down by classroom (i.e., output a list of classrooms ordered by classroom number, with a total number of students in each of the classrooms).
---
`Command: E[nrollment]`
`Example: E`

Requirement NR5. Add to your program the commands that allow a data analyst to extract appropriate data to be able to analyze whether student GPAs are affected by the student’s grades, student’s teachers or the bus routes the students are on.
---
`Command: 	P[erformance]: G[rade] <number>`
`P[erformance]: T[eacher] <LastName>`
`P[erformance]: B[us] <number>`

`Example: 	P: G 6`
`P: T Cool`
`P: Bus 52`
