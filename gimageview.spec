Summary:	Graphic Viewer
Summary(pl):	Przeglądarka plików graficznych 
Name:		gimageview
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://west.dl.sourceforge.net/sourceforge/gtkmmviewer/%{name}-%{version}.tar.gz
URL:		http://www.homa.ne.jp/~ashie/gimageview/
BuildRequires:	gtk+-devel 
BuildRequires:  imlib-devel
Requires:	glib >= 1.2.6
Requires:  	gtk+ >= 1.2.6
Requires:	imlib >= 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GImageView is a GTK+ based image viewer. It support tabbed browsing,
thumbnail table views, directory tree views, drag and drop, reading
thumbnail cache of other famous image viewers, and flexible user
interface.

%description -l pl
GImageView to bazujaca na GTK+ przeglądarka obrazków. Pozwala na
przeglądanie z zakładkami, przeglądanie miniaturek i drzew katalogów,
obsługuje drag-n-drop, potrafi odczytywać miniaturki z cache innych
przeglądarek obrazków i ma elastyczny interfejs użytkownika.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf AUTHORS ChangeLog README TIPS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gimv
%dir %{_datadir}/gimageview
%dir %{_datadir}/gimageview/pixmaps
%dir %{_datadir}/gimageview/pixmaps/default
%{_datadir}/gimageview/pixmaps/default/*.xpm
%dir %{_libdir}/gimageview
%dir %{_libdir}/gimageview/*
%attr(755,root,root) %{_libdir}/gimageview/*/*.so
