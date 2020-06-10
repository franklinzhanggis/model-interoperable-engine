#Data : 2020-5-28
#Author : Fengyuan Zhang (Franklin)
#Email : franklinzhang@foxmail.com
#Description : this component is used to wrap OpenGMS service



from ogmsservice import OGMSService_DEBUG as ogms
from typing import Tuple
from bmi import Bmi
import numpy as np
import json
import sys
import os


class OGMSService(Bmi):
    def __init__(self):
        self._service = None
        self._ac = None
        self._inputs = []
        self._outputs = []
        
    def bindOGMSService(self, host: str, port: int, serviceid: str) -> bool:
        server = ogms.CreateServer(host, port)
        self._ac = server.getServiceAccess()
        self._service = self._ac.getModelServiceByID(serviceid)

    #! BMI interface
    def initialize(self, config_file: str) -> None:
        pass

    def update(self) -> None:
        msrid = self._service.invoke(self._inputs)
        msr = self._ac.getModelServiceRunningRecordByID(msrid)
        msr.wait4Finished()
        for op in msr.outputs:
            self._outputs.append(op)


    def finalize(self) -> None:
        pass

    def get_component_name(self) -> str:
        self._service.name

    def get_input_var_names(self) -> Tuple[str]:
        strMDL = self._service.xml
        jsMDL = json.loads(strMDL)
        inputs = []
        states = jsMDL["ModelClass"]["Behavior"]["StateGroup"]["States"]["State"]
        for state in states:
            for event in state["Event"]:
                if event["$"]["type"] == "response":
                    inputs.append(state["$"]["name"] + "-" + event["$"]["name"])
        return inputs

    def get_output_var_names(self) -> Tuple[str]:
        strMDL = self._service.xml
        jsMDL = json.loads(strMDL)
        outputs = []
        states = jsMDL["ModelClass"]["Behavior"]["StateGroup"]["States"]["State"]
        for state in states:
            for event in state["Event"]:
                if event["$"]["type"] == "noresponse":
                    outputs.append(state["$"]["name"] + "-" + event["$"]["name"])
        return outputs

    def get_var_grid(self, name: str) -> int:
        pass

    def get_var_type(self, name: str) -> str:
        pass

    def get_var_units(self, name: str) -> str:
        pass

    def get_var_itemsize(self, name: str) -> int:
        pass

    def get_var_nbytes(self, name: str) -> int:
        pass

    def get_var_location(self, name: str) -> str:
        pass
    
    def get_current_time(self) -> float:
        pass

    def get_start_time(self) -> float:
        pass

    def get_end_time(self) -> float:
        pass

    def get_time_units(self) -> str:
        pass

    def get_time_step(self) -> float:
        pass

    def get_value(self, name: str, dest: np.ndarray) -> np.ndarray:
        params = name.split("-")
        stateName = params[0]
        eventName = params[1]
        data = None
        for ip in self._inputs:
            if ip.stateName == stateName and ip.eventName == eventName:
                data = self._ac.getDataByID(ip.dataid)
        for op in self._outputs:
            if op.stateName == stateName and op.eventName == eventName:
                data = self._ac.getDataByID(ip.dataid)
        if data == None:
            return None
        data.save("./tmp.dat")
        if dest:
            dest = np.loadtxt("./tmp.dat")
        value = np.loadtxt("./tmp.dat")
        return value

    def get_value_ptr(self, name: str) -> np.ndarray:
        pass

    def get_value_at_indices(self, name: str, dest: np.ndarray, inds: np.ndarray) -> np.ndarray:
        pass

    def set_value(self, name: str, values: np.ndarray) -> None:
        params = name.split("-")
        stateName = params[0]
        eventName = params[1]
        np.savetxt("./tmp.dat", values)
        dataid = self._ac.uploadDataByFile(stateName + "-" + eventName, "./tmp.dat")
        os.remove("./tmp.dat")
        for ip in self._inputs:
            if ip.stateName == stateName and ip.eventName == eventName:
                ip.dataid = dataid
                return
        datacfg = self._ac.createDataConfigurationItem(stateName, eventName, dataid)
        self._inputs.append(datacfg)
        return
        

    def set_value_at_indices(self, name: str, inds: np.ndarray, src: np.ndarray) -> None:
        pass

    def get_grid_rank(self, grid: int) -> int:
        pass

    def get_grid_size(self, grid: int) -> int:
        pass

    def get_grid_type(self, grid: int) -> str:
        pass

    def get_grid_shape(self, grid: int, shape: np.ndarray) -> np.ndarray:
        pass

    def get_grid_spacing(self, grid: int, spacing: np.ndarray) -> np.ndarray:
        pass

    def get_grid_origin(self, grid: int, origin: np.ndarray) -> np.ndarray:
        pass

    def get_grid_x(self, grid: int, x: np.ndarray) -> np.ndarray:
        pass

    def get_grid_y(self, grid: int, y: np.ndarray) -> np.ndarray:
        pass

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        pass

    def get_grid_node_count(self, grid: int) -> int:
        pass

    def get_grid_edge_count(self, grid: int) -> int:
        pass

    def get_grid_face_count(self, grid: int) -> int:
        pass

    def get_grid_edge_nodes(self, grid: int, edge_nodes: np.ndarray) -> np.ndarray:
        pass

    def get_grid_face_nodes(self, grid: int, face_nodes: np.ndarray) -> np.ndarray:
        pass

    def get_grid_nodes_per_face(self, grid: int, nodes_per_face: np.ndarray) -> np.ndarray:
        pass


svc = OGMSService()
svc.bindOGMSService("172.21.212.103", 8060, "5eb19b154b1d6302ac0637ce")
inputs = svc.get_input_var_names()
print(inputs)
outputs = svc.get_output_var_names()
print(outputs)
