import flet as ft


def main(page: ft.Page):
    page.title="Posters"
    page.bgcolor=ft.colors.WHITE
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.window.min_height=800
    page.window.min_width=450
    page.window.always_on_top=True
    


    posters=[f'images/poster_{index}.jpg' for index in range(1, 11)]
    
    def posters_adjusts():
        for item in layout.controls:
            if item.data < 0:
                pass
            else:
                if item.content.opacity - item.data*0.3 < 0:
                    value=0
                else:
                    value=item.content.opacity - item.data*0.3
                
                item.content.offset.x += item.data*0.2
                item.content.scale -= item.data*0.1
                item.content.opacity = value

        page.update()


    def handle_dismiss(e):
        for pos, item in enumerate(layout.controls):
            
            if e.control == layout.controls[0]:
                layout.controls.clear()
                layout.controls.extend(
                    [
                        ft.Dismissible(
                            content=ft.Container(
                                image_src=image,
                                image_fit=ft.ImageFit.COVER,
                                border_radius=20,
                                aspect_ratio=9/16,
                                shadow=ft.BoxShadow(blur_radius=40),
                                offset=ft.Offset(x=0, y=0),
                                scale=1,
                                opacity=1,
                                animate=ft.Animation(duration=500, curve=ft.AnimationCurve.DECELERATE),
                                animate_offset=True,
                                animate_opacity=True,
                                animate_scale=True,
                            ),
                            data=index,
                            on_dismiss=handle_dismiss
                        ) for index, image in reversed(list(enumerate(posters)))
                    ]
                )
                break

            else:
                item.data-=1
                item.content.scale=1
                item.content.opacity=1
                item.content.offset.x=0
        
        posters_adjusts()



    layout = ft.Stack(
        alignment=ft.alignment.center,
        height=450,
        controls=[
            ft.Dismissible(
                content=ft.Container(
                    image_src=image,
                    image_fit=ft.ImageFit.COVER,
                    border_radius=20,
                    aspect_ratio=9/16,
                    shadow=ft.BoxShadow(blur_radius=40),
                    offset=ft.Offset(x=0, y=0),
                    scale=1,
                    opacity=1,
                    animate=ft.Animation(duration=500, curve=ft.AnimationCurve.DECELERATE),
                    animate_offset=True,
                    animate_opacity=True,
                    animate_scale=True,
                ),
                data=index,
                on_dismiss=handle_dismiss
            ) for index, image in reversed(list(enumerate(posters)))
        ]
    )


    

    page.add(layout)

    posters_adjusts()


ft.app(target=main, assets_dir='assets')