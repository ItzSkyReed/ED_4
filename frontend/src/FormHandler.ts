export default class FormHandler {
    private static createJSON(data: any): string {
        return JSON.stringify(data);
    }

    public static async sendFormData(data: any): Promise<void> {
        const jsonData = this.createJSON(data);

        try {
            const response = await fetch('http://localhost:8000/post/send_json', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: jsonData,
            });

            if (response.ok) {
                alert("Успешная Отправка!");
            } else {
                const errorData = await response.json();
                throw new Error(errorData.error);
            }
        } catch (error: any) {
            alert(error.message);
        }
    }
}