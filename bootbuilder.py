import os
import subprocess
import psutil
import platform

class BootBuilder:
    def __init__(self):
        self.system_os = platform.system()

    def check_os(self):
        if self.system_os != "Windows":
            raise EnvironmentError("BootBuilder is only compatible with Windows OS.")

    def optimize_startup_programs(self):
        """Disables unnecessary startup programs for faster boot times."""
        print("Optimizing startup programs...")
        startup_folder = os.getenv('APPDATA') + r'\Microsoft\Windows\Start Menu\Programs\Startup'
        try:
            for item in os.listdir(startup_folder):
                file_path = os.path.join(startup_folder, item)
                if os.path.isfile(file_path):
                    os.rename(file_path, file_path + ".disabled")
                    print(f"Disabled: {item}")
            print("Startup programs optimized.")
        except Exception as e:
            print(f"Error optimizing startup programs: {e}")

    def manage_services(self):
        """Optimizes Windows services for better performance."""
        print("Managing services...")
        try:
            services_to_optimize = ["wuauserv", "SysMain", "Fax", "diagnosticshub.standardcollector.service"]
            for service in services_to_optimize:
                subprocess.run(['sc', 'config', service, 'start=disabled'], check=True)
                print(f"Service '{service}' disabled.")
            print("Services managed successfully.")
        except Exception as e:
            print(f"Error managing services: {e}")

    def clean_temp_files(self):
        """Cleans temporary files to free up disk space."""
        print("Cleaning temporary files...")
        temp_dir = os.getenv('TEMP')
        try:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Removed temp file: {file}")
            print("Temporary files cleaned.")
        except Exception as e:
            print(f"Error cleaning temporary files: {e}")

    def optimize_performance(self):
        """Executes all optimization functions."""
        self.check_os()
        print("Starting boot optimization process...")
        self.optimize_startup_programs()
        self.manage_services()
        self.clean_temp_files()
        print("Boot optimization process completed.")

if __name__ == "__main__":
    builder = BootBuilder()
    builder.optimize_performance()