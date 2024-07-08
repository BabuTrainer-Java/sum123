FROM python  
COPY . /core_python_programs
CMD ["python", "/core_python_programs/str_funs_demo.py"]  
